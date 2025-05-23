"""empty message

Revision ID: 185ff26c887d
Revises: eb2082f34b58
Create Date: 2025-05-07 22:30:10.099598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '185ff26c887d'
down_revision = 'eb2082f34b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
