from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import CreateView, ListView, UpdateView

from .models import Review, TalkProposal


class TalkProposalListView(PermissionRequiredMixin, ListView):

    model = TalkProposal
    permission_required = 'reviews.add_review'
    template_name = 'reviews/talk_proposal_list.html'

    def get_queryset(self):
        user = self.request.user
        unreviewed = self.model.objects.filter_reviewable(user).exclude(
            review__reviewer=user,
        )
        return unreviewed.order_by('?')


class ReviewCreateView(PermissionRequiredMixin, CreateView):

    model = Review
    permission_required = 'reviews.add_review'
    template_name = 'reviews/review_form.html'
    fields = ('score', 'comment', 'note', )

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        proposal_id = self.request.GET.get('proposal_id')
        try:
            context['proposal'] = TalkProposal.objects.get(pk=proposal_id)
        except TalkProposal.DoesNotExist:
            raise Http404('Proposal not found!')

        if context['proposal'].submitter == self.request.user:
            raise PermissionDenied

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.reviewer = self.request.user
        proposal_id = self.request.GET.get('proposal_id')
        self.object.proposal = TalkProposal.objects.get(pk=proposal_id)
        return super(ReviewCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('review_proposal_list')


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):

    model = Review
    permission_required = 'reviews.add_review'
    fields = ('score', 'comment', 'note', )
    template_name = 'reviews/review_form.html'

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReviewUpdateView, self).get_context_data(**kwargs)
        context['proposal'] = self.object.proposal
        return context

    def get_success_url(self):
        return reverse('review_proposal_list')
