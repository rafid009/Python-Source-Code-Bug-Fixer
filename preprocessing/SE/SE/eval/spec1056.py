import numpy as np 

def function(x):

	j8 = x
	t0 = x
	paths = []
	try:
		if x < 5:
			x = x+x
			paths.append(1)
		else:
			t0 = 3-t0
			j8 = 8/j8
			paths.append(2)
		if j8 <= 0:
			x = 6+1
			x = t0*5
			paths.append(3)
		else:
			t0 = x+3
			t0 = t0/6
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