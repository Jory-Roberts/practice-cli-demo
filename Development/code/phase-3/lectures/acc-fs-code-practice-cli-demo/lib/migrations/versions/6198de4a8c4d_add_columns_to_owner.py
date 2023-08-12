"""add columns to owner

Revision ID: 6198de4a8c4d
Revises: 12a7a438ee41
Create Date: 2023-08-11 08:21:07.443472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6198de4a8c4d'
down_revision = '12a7a438ee41'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('city', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('state', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('zip_code', sa.String(), nullable=True))
        batch_op.create_unique_constraint('uq_email', ['email'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.drop_constraint('uq_email', type_='unique')
        batch_op.drop_column('zip_code')
        batch_op.drop_column('state')
        batch_op.drop_column('city')
        batch_op.drop_column('address')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('email')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###
