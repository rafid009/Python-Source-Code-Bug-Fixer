import numpy as np 

def function(x):

	o4 = x
	j5 = 3
	paths = []
	try:
		if o4 < 4:
			x = 8/x
			x = 0+x
			paths.append(1)
		else:
			o4 = o4/2
			o4 = 3-0
			j5 = j5*0
			paths.append(2)
		if o4 <= 3:
			j5 = j5*1
			j5 = j5+4
			j5 = j5-7
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))