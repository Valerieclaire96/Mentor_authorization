"""empty message

Revision ID: 794a780696b1
Revises: a65cce66969f
Create Date: 2023-05-27 13:55:22.539685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '794a780696b1'
down_revision = 'a65cce66969f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
