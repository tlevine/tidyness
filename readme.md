Here I model our determination of how tidy a dataset is.
My goal in this is to determine whether a dataset is tidy
so that someone can know to fix it if it's not.

Hadley Wickham (1) presents five ways in which a dataset
might be untidy.

1. column headers are values, not variable names
2. multiple variables are stored in one colum
3. variables are stored in both rows and columns
4. multiple types of observational unit are stored in the same table
5. a single observational unit is stored in multiple tables

I try to detect all of these, in order because that's easiest.

## References

1. http://vita.had.co.nz/papers/tidy-data.pdf
2. http://stat405.had.co.nz/lectures/18-tidy-data.pdf
