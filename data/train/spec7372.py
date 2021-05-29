import numpy as np 

def function(x):

	t3 = 7
	j0 = 0
	paths = []
	try:
		if j0 >= 9:
			x = t3+x
			paths.append(1)
		else:
			x = x-t3
			j0 = x+3
			paths.append(2)
		if j0 > 4:
			j0 = x*4
			j0 = j0-8
			x = j0/8
			paths.append(3)
		else:
			x = 5-j0
			t3 = x*t3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		t3 = j0**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))