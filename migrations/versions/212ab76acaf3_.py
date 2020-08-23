"""empty message

Revision ID: 212ab76acaf3
Revises: e01d6666eeb5
Create Date: 2020-08-23 10:09:55.528596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '212ab76acaf3'
down_revision = 'e01d6666eeb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructor', sa.Column('name', sa.String(), nullable=True))
    op.add_column('instructor', sa.Column('qualifiaction', sa.String(), nullable=True))
    op.drop_column('instructor', 'email')
    op.drop_column('instructor', 'lanme')
    op.drop_column('instructor', 'fname')
    op.drop_column('instructor', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructor', sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('instructor', sa.Column('fname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('instructor', sa.Column('lanme', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('instructor', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('instructor', 'qualifiaction')
    op.drop_column('instructor', 'name')
    # ### end Alembic commands ###
