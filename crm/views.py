from django.shortcuts import render, redirect, get_object_or_404
from .models import Deal


STAGES = [
    ('lead', 'Lead'),
    ('diagnostico', 'Diagnóstico'),
    ('proposta', 'Proposta'),
    ('negociacao', 'Negociação'),
    ('fechado', 'Fechado'),
]


def pipeline_view(request):
    pipeline_data = []

    for stage_key, stage_label in STAGES:
        deals = Deal.objects.filter(stage=stage_key, status='aberta')
        total_value = sum(deal.value or 0 for deal in deals)

        pipeline_data.append({
            'key': stage_key,
            'label': stage_label,
            'deals': deals,
            'count': deals.count(),
            'total_value': total_value,
        })

    return render(request, 'crm/pipeline.html', {'pipeline_data': pipeline_data})


def move_deal_stage(request, deal_id, direction):
    deal = get_object_or_404(Deal, id=deal_id)

    stage_keys = [stage[0] for stage in STAGES]

    try:
        current_index = stage_keys.index(deal.stage)
    except ValueError:
        return redirect('pipeline')

    if direction == 'forward' and current_index < len(stage_keys) - 1:
        deal.stage = stage_keys[current_index + 1]
        deal.save()

    elif direction == 'backward' and current_index > 0:
        deal.stage = stage_keys[current_index - 1]
        deal.save()

    return redirect('pipeline')

def move_deal_to_stage(request, deal_id, stage):
    deal = get_object_or_404(Deal, id=deal_id)

    valid_stages = [s[0] for s in STAGES]

    if stage in valid_stages:
        deal.stage = stage
        deal.save()

    return redirect('pipeline')