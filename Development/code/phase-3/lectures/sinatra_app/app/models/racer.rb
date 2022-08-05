class Racer < ActiveRecord::Base
  # attr_accessor :name, :team, :number, :nationality, :id

  # @@all = []
  # @@count = 0

  # def initialize(args = {})
  #   args.each do |k, v|
  #     self.send("#{k}=", v)
  #   end
  # end

  # def save
  #   self.id = @@count
  #   @@count += 1
  #   @@all << self
  # end

  # def self.create(args = {})
  #   racer = self.new(args)
  #   racer.save
  # end

  # def self.find(id)
  #   @@all.find { |r| r.id == id }
  # end

  # def self.all
  #   @@all
  # end
end


