"""empty message

Revision ID: 2ed991737b9e
Revises: 5cf107cc039f
Create Date: 2023-12-20 13:55:26.744169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ed991737b9e'
down_revision = '5cf107cc039f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_days', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('completed_days')

    # ### end Alembic commands ###
