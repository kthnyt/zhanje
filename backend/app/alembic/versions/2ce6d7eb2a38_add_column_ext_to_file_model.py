"""Add column ext to File model

Revision ID: 2ce6d7eb2a38
Revises: 4d550044f487
Create Date: 2021-08-11 19:25:15.375251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce6d7eb2a38'
down_revision = '4d550044f487'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('ext', sa.String(), nullable=True))
    op.drop_index('ix_file_source', table_name='file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_file_source', 'file', ['source'], unique=False)
    op.drop_column('file', 'ext')
    # ### end Alembic commands ###