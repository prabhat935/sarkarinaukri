"""
Helpers for the seed commands that run on every deploy.

Django's update_or_create() saves every row each time, which resets
`updated_at` and makes every guide look "updated today" after each deploy.
upsert() only writes when a value actually changed, so "Last updated" dates,
the sitemap's lastmod and the structured data's dateModified stay truthful.
"""


def upsert(model, defaults=None, **lookup):
    """Create the row if missing; otherwise save only if a field changed.
    Returns (obj, created) like update_or_create()."""
    defaults = defaults or {}
    obj = model.objects.filter(**lookup).first()
    if obj is None:
        return model.objects.create(**lookup, **defaults), True
    changed = [field for field, value in defaults.items() if getattr(obj, field) != value]
    if changed:
        for field in changed:
            setattr(obj, field, defaults[field])
        obj.save()
    return obj, False
