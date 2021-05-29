import numpy as np 

def function(x):

	j8 = x
	o4 = 0
	x = 9
	paths = []
	try:
		if x > 8:
			x = 1-x
			j8 = j8+0
			x = x*2
			paths.append(1)
		else:
			x = j8-x
			paths.append(2)
		if o4 < 0:
			j8 = o4-4
			x = x/7
			o4 = 5+o4
			paths.append(3)
		else:
			o4 = 0*o4
			j8 = 2+0
			j8 = j8-5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))