## 1. Introduction ##

mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Trust' }
happiness2015 = happiness2015.rename(mapping,axis=1)

## 2. Apply a Function Element-wise Using the Map and Apply Methods ##

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
   
    
economy_impact_map = happiness2015['Economy'].map(label)
economy_impact_apply = happiness2015['Economy'].apply(label)
equal = economy_impact_map.equals(economy_impact_apply)

## 3. Apply a Function Element-wise Using the Map and Apply Methods Continued ##

def label(element, x):
    if element > x:
        return 'High'
    else:
        return 'Low'
economy_impact_apply = happiness2015['Economy'].apply(label, x=.8)

## 4. Apply a Function Element-wise to Multiple Columns Using Applymap Method ##

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
economy_apply = happiness2015['Economy'].apply(label)
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
factors_impact = happiness2015[factors].applymap(label)

## 5. Apply Functions along an Axis using the Apply Method ##

def v_counts(col):
    num = col.value_counts()
    den = col.size
    return num/den

v_counts_pct = factors_impact.apply(v_counts)