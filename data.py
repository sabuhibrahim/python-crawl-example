
# Example datas with real urls
SHOPS = [
    {
        'name': 'Trendyol',
        'url': 'https://www.trendyol.com/nike/nk3285507-basketbol-topu-280-p-3573517',
        'keyword': 'prc-dsc', # value of html element's attribute. 
        'element': 'span', # html element
        'attr': 'class' # name of html element's attribute. 
    },
    {
        'name': 'DeFacto',
        'url': 'https://www.defacto.com.tr/slim-fit-poplin-uzun-kollu-gomlek-2456713',
        'keyword': 'product-card__price--new',
        'element': 'div',
        'attr': 'class'
    },
    {
        'name': 'Hepsiburada',
        'url': 'https://www.hepsiburada.com/lego-classic-213-parcalik-yaratici-canta-yapim-parcalari-kutusu-10713-cocuk-oyuncak-yapim-seti-p-HBV000009OFR2?magaza=Hepsiburada',
        'keyword': 'markupText:\'currentPriceBeforePoint\'',
        'element': 'span',
        'attr': 'data-bind'
    },
]