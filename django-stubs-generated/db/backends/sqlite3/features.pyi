from typing import Optional

from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    connection: django.db.backends.sqlite3.base.DatabaseWrapper
    can_use_chunked_reads: bool = ...
    test_db_allows_multiple_connections: bool = ...
    supports_unspecified_pk: bool = ...
    supports_timezones: bool = ...
    max_query_params: int = ...
    supports_mixed_date_datetime_comparisons: bool = ...
    supports_column_check_constraints: bool = ...
    autocommits_when_autocommit_is_off: bool = ...
    can_introspect_decimal_field: bool = ...
    can_introspect_positive_integer_field: bool = ...
    can_introspect_small_integer_field: bool = ...
    supports_transactions: bool = ...
    atomic_transactions: bool = ...
    can_rollback_ddl: bool = ...
    supports_atomic_references_rename: bool = ...
    supports_paramstyle_pyformat: bool = ...
    supports_sequence_reset: bool = ...
    can_clone_databases: bool = ...
    supports_temporal_subtraction: bool = ...
    ignores_table_name_case: bool = ...
    supports_cast_with_precision: bool = ...
    uses_savepoints: bool = ...
    can_release_savepoints: bool = ...
    def supports_stddev(self) -> bool: ...