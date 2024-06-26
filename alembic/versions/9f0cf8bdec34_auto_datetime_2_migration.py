"""auto datetime 2 migration

Revision ID: 9f0cf8bdec34
Revises: 1e760eae6fdb
Create Date: 2024-01-30 21:27:06.643259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f0cf8bdec34'
down_revision = '1e760eae6fdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_column('create_date')

    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###
