# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.filemap import FileMap  # noqa
from app.models.platform import Platform # noqa
from app.models.mrd_order import MrDOrder  # noqa
