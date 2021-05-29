import numpy as np 

def function(x):

	h6 = 0
	j5 = 7
	paths = []
	try:
		if x > 2:
			x = x*2
			x = 2+x
			paths.append(1)
		else:
			h6 = h6+5
			j5 = j5+0
			paths.append(2)
		if h6 >= 5:
			j5 = j5/4
			h6 = 7*3
			x = 1-8
			paths.append(3)
		else:
			j5 = j5*2
			h6 = h6-7
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		j5 = h6**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))