import numpy as np 

def function(x):

	t2 = 3
	j8 = 0
	x = x
	paths = []
	try:
		if j8 < 4:
			j8 = 6-8
			t2 = t2-3
			x = x/8
			paths.append(1)
		else:
			x = x+j8
			x = 8+j8
			paths.append(2)
		if j8 >= 5:
			t2 = t2-3
			paths.append(3)
		else:
			t2 = t2*x
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