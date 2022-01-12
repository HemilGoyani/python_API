"""saved table for parent and child

Revision ID: 2c84749c3511
Revises: c2005fcf9be0
Create Date: 2022-01-11 04:03:09.771204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c84749c3511'
down_revision = 'c2005fcf9be0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('mobileno', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parent_address'), 'parent', ['address'], unique=False)
    op.create_index(op.f('ix_parent_id'), 'parent', ['id'], unique=False)
    op.create_index(op.f('ix_parent_mobileno'), 'parent', ['mobileno'], unique=False)
    op.create_index(op.f('ix_parent_name'), 'parent', ['name'], unique=True)
    op.create_table('child',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_child_id'), 'child', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_child_id'), table_name='child')
    op.drop_table('child')
    op.drop_index(op.f('ix_parent_name'), table_name='parent')
    op.drop_index(op.f('ix_parent_mobileno'), table_name='parent')
    op.drop_index(op.f('ix_parent_id'), table_name='parent')
    op.drop_index(op.f('ix_parent_address'), table_name='parent')
    op.drop_table('parent')
    # ### end Alembic commands ###