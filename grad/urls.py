from django.conf.urls import url
from courselib.urlparts import LETTER_TEMPLATE_SLUG, GRAD_SLUG, LETTER_TEMPLATE_ID, LETTER_SLUG

grad_patterns = [ # prefix /grad/
    url(r'^$', 'grad.views.index'),
    #url(r'^import$', 'grad.views.import_applic'),
    url(r'^progress_reports', 'grad.views.progress_reports'),
    url(r'^search$', 'grad.views.search'),
    url(r'^search/save$', 'grad.views.save_search'),
    url(r'^search/delete$', 'grad.views.delete_savedsearch'),
    url(r'^qs', 'grad.views.quick_search'),

    url(r'^program/new$', 'grad.views.new_program'),
    url(r'^program/$', 'grad.views.programs'),
    url(r'^requirement/$', 'grad.views.requirements'),
    url(r'^requirement/new$', 'grad.views.new_requirement'),

    url(r'^letterTemplates/$', 'grad.views.letter_templates'),
    url(r'^letterTemplates/new', 'grad.views.new_letter_template'),
    url(r'^letterTemplates/' + LETTER_TEMPLATE_SLUG + '/manage', 'grad.views.manage_letter_template'),
    url(r'^promises/$', 'grad.views.all_promises'),
    url(r'^promises/(?P<semester_name>\d{4})$', 'grad.views.all_promises'),
    url(r'^funding/$', 'grad.views.funding_report'),
    url(r'^funding/(?P<semester_name>\d{4})$', 'grad.views.funding_report'),

    url(r'^' + GRAD_SLUG + '/$', 'grad.views.view'),
    url(r'^' + GRAD_SLUG + '/moreinfo$', 'grad.views.grad_more_info'),
    url(r'^' + GRAD_SLUG + '/general$', 'grad.views.manage_general'),
    url(r'^' + GRAD_SLUG + '/program', 'grad.views.manage_program'),
    url(r'^' + GRAD_SLUG + '/start_end', 'grad.views.manage_start_end_semesters'),
    url(r'^' + GRAD_SLUG + '/defence', 'grad.views.manage_defence'),
    url(r'^' + GRAD_SLUG + '/form', 'grad.views.get_form'),
    url(r'^' + GRAD_SLUG + '/supervisors$', 'grad.views.manage_supervisors'),
    url(r'^' + GRAD_SLUG + '/supervisors/(?P<sup_id>\d+)/remove$', 'grad.views.remove_supervisor'),
    url(r'^' + GRAD_SLUG + '/status$', 'grad.views.manage_status'),
    url(r'^' + GRAD_SLUG + '/status/(?P<s_id>\d+)/remove$', 'grad.views.remove_status'),
    url(r'^' + GRAD_SLUG + '/requirements$', 'grad.views.manage_requirements'),
    url(r'^' + GRAD_SLUG + '/requirements/(?P<cr_id>\d+)/remove$', 'grad.views.remove_completedrequirement'),
    url(r'^' + GRAD_SLUG + '/otherfunding$', 'grad.views.manage_otherfunding'),
    url(r'^' + GRAD_SLUG + '/otherfunding/(?P<o_id>\d+)/remove$', 'grad.views.remove_otherfunding'),
    url(r'^' + GRAD_SLUG + '/financial$', 'grad.views.financials'),
    url(r'^' + GRAD_SLUG + '/financialcomments$', 'grad.views.manage_financialcomments'),
    url(r'^' + GRAD_SLUG + '/financialcomments/(?P<f_id>\d+)/remove$', 'grad.views.remove_financialcomment'),
    url(r'^' + GRAD_SLUG + '/promises$', 'grad.views.manage_promises'),
    url(r'^' + GRAD_SLUG + '/promises/(?P<p_id>\d+)/remove$', 'grad.views.remove_promise'),
    url(r'^' + GRAD_SLUG + '/scholarship$', 'grad.views.manage_scholarships'),
    url(r'^' + GRAD_SLUG + '/scholarship/(?P<s_id>\d+)/remove$', 'grad.views.remove_scholarship'),
    url(r'^' + GRAD_SLUG + '/letters$', 'grad.views.manage_letters'),
    url(r'^' + GRAD_SLUG + '/letters/' + LETTER_TEMPLATE_SLUG + '/new$', 'grad.views.new_letter'),
    url(r'^' + GRAD_SLUG + '/letters/_get_text/' + LETTER_TEMPLATE_ID + '$', 'grad.views.get_letter_text'),
    url(r'^' + GRAD_SLUG + '/letters/' + LETTER_SLUG + '$', 'grad.views.get_letter'),
    url(r'^' + GRAD_SLUG + '/letters/' + LETTER_SLUG + '/view$', 'grad.views.view_letter'),
    url(r'^' + GRAD_SLUG + '/letters/' + LETTER_SLUG + '/copy', 'grad.views.copy_letter'),
    url(r'^get_addresses$', 'grad.views.get_addresses'),
    url(r'^scholarship_types$', 'grad.views.manage_scholarshipType'),
    url(r'^financial_summary$', 'grad.views.student_financials'),
    #url(r'^new', 'grad.views.new'),
    url(r'^found', 'grad.views.not_found'),
]