CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size FROM dogs, sizes 
  WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.child FROM parents AS a, dogs AS b WHERE a.parent = b.name ORDER BY  b.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.parent AS parent, a.child AS sibling, b.size AS size FROM parents AS a, size_of_dogs AS b 
  WHERE a.child = b.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sibling || ' and ' || b.sibling || ' are ' || a.size || ' siblings' FROM siblings AS a, siblings AS b 
  WHERE a.parent = b.parent AND a.size = b.size AND a.sibling < b.sibling;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT name, height, height FROM dogs;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ', ' || b.dogs || ', ' || c.dogs || ', ' || d.dogs,
  a.stack_height + b.stack_height + c.stack_height + d.stack_height, d.stack_height
  FROM stacks_helper AS a, stacks_helper AS b, stacks_helper AS c, stacks_helper AS d 
  WHERE a.last_height < b.last_height AND b.last_height < c.last_height AND c.last_height < d.last_height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE stack_height >= 170 ORDER BY stack_height;
