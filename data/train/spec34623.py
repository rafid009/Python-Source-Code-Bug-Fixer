import numpy as np 

def function(x):

	e8 = x
	j1 = x
	paths = []
	try:
		if j1 <= 7:
			j1 = j1+x
			x = x/x
			e8 = e8+2
			paths.append(1)
		else:
			j1 = j1-5
			paths.append(2)
		if e8 < 4:
			x = 2/6
			x = 5/9
			x = x-2
			paths.append(3)
		else:
			e8 = j1/e8
			e8 = 7*e8
			e8 = e8-9
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		j1 = e8**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))