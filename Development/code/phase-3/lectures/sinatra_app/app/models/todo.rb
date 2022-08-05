class Todo < ActiveRecord::Base
    # Todo.all
    # Todo.first
    # Todo.last
    # Todo.create
    belongs_to :user
end