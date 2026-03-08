# 15. Forward Chaining
def forward_chaining(rules, facts):
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(c in facts for c in conditions) and conclusion not in facts:
                facts.add(conclusion); changed = True
    return facts

rules = [({'mammal','has_hair'}, 'dog'), ({'dog'}, 'pet'), ({'pet'}, 'friendly')]
facts = {'mammal','has_hair'}
print("Forward Chaining:", forward_chaining(rules, facts))