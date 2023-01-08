from django.shortcuts import render

from .forms import CalcForm


def main_calc(request):
    form = CalcForm(request.POST)

    submitbutton = request.POST.get("submit")

    form = CalcForm(request.POST or None)
    if form.is_valid():
        qualification = form.cleaned_data.get("qualification")
        quantity = form.cleaned_data.get("quantity")
        deal_1 = form.cleaned_data.get("deal_1")
        deal_2 = form.cleaned_data.get("deal_2")
        deal_3 = form.cleaned_data.get("deal_3")
        deal_4 = form.cleaned_data.get("deal_4")
        deal_5 = form.cleaned_data.get("deal_5")
        deal_6 = form.cleaned_data.get("deal_6")

        summ_deal = deal_6 + deal_5 + deal_4 + deal_3 + deal_2 + deal_1

        if quantity > 1:
            if quantity == 2:
                motivation = 1.2
            if quantity == 3:
                motivation = 1.3
            if quantity == 4:
                motivation = 1.4
            if quantity >= 5:
                motivation = 1.5
            gross_salary = ((summ_deal / 100 * qualification) * motivation)
            tax = gross_salary * 0.13
            result = gross_salary - tax




    context = {
        'form': form,
        'result': result,
        'submitbutton': submitbutton,
    }

    return render(request,
                  'calculator/calc.html',
                  context)

