from dataclasses import dataclass


@dataclass(frozen=True)
class Configuration:
    """
    This data class stores the configuration per each evidence type.
    Parameters:
        collection - The collection name in the DB
        fields - The field to be store in each dict of parsed data
    """
    evidence_type_1 = dict(collection='evidence_type_1',
                           fields=dict(
                               user_details=('id', 'email', 'full_name', 'updated_at'),
                               security=("mfa_enabled")
                                )
                           )
