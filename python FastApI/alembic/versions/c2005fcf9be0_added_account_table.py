"""Added account table

Revision ID: c2005fcf9be0
Revises: 
Create Date: 2022-01-10 05:30:25.582212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2005fcf9be0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Users1_email', table_name='Users1')
    op.drop_index('ix_Users1_id', table_name='Users1')
    op.drop_table('Users1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users1',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users1_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Users1_pkey')
    )
    op.create_index('ix_Users1_id', 'Users1', ['id'], unique=False)
    op.create_index('ix_Users1_email', 'Users1', ['email'], unique=False)
    # ### end Alembic commands ###