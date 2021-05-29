import numpy as np 

def function(x):

	j2 = 6
	t1 = x
	paths = []
	try:
		if j2 <= 9:
			j2 = x+j2
			j2 = j2+2
			paths.append(1)
		else:
			t1 = 0+6
			x = x/x
			paths.append(2)
		if t1 < 2:
			j2 = 3*j2
			x = t1*5
			paths.append(3)
		else:
			j2 = 7-x
			t1 = 4-5
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))