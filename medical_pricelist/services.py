from gettext import gettext as _


def set_pricelist_deleted(pricelist):
    """
    Marks a price list as deleted
    :param pricelist: the object to mark as deleted
    :return: an empty array is everything goes well, an array with errors if any
    """
    try:
        pricelist.delete_history()
        return []
    except Exception:
        return {
            "title": pricelist.uuid,
            "list": [
                {
                    "message": _(
                        f"pricelist.mutation.failed_to_delete_{pricelist.model_prefix}"
                    )
                    % {"uuid": pricelist.uuid},
                    "detail": pricelist.uuid,
                }
            ],
        }
