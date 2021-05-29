import numpy as np 

def function(x):

	t3 = 7
	j1 = x
	paths = []
	try:
		if t3 > 6:
			j1 = j1+0
			x = t3/x
			t3 = t3*4
			paths.append(1)
		else:
			t3 = t3/t3
			j1 = j1/3
			t3 = t3+2
			paths.append(2)
		if x > 9:
			j1 = j1-t3
			x = x/8
			paths.append(3)
		else:
			t3 = x*t3
			x = 7-t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))