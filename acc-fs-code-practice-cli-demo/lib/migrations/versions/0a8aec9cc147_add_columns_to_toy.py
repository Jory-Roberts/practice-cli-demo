"""add columns to toy

Revision ID: 0a8aec9cc147
Revises: 6198de4a8c4d
Create Date: 2023-08-11 08:28:26.213908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8aec9cc147'
down_revision = '6198de4a8c4d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('toy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('manufacturer', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('type', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('location', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('notes', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('is_favorite', sa.Boolean(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('toy', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('is_favorite')
        batch_op.drop_column('notes')
        batch_op.drop_column('location')
        batch_op.drop_column('type')
        batch_op.drop_column('manufacturer')

    # ### end Alembic commands ###
