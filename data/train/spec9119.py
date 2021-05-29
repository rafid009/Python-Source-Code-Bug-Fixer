import numpy as np 

def function(x):

	t2 = x
	j2 = 8
	paths = []
	try:
		if j2 < 5:
			t2 = t2/3
			t2 = 9*3
			j2 = j2-x
			paths.append(1)
		else:
			t2 = t2-7
			paths.append(2)
		if t2 <= 2:
			x = x-8
			t2 = 3+t2
			paths.append(3)
		else:
			j2 = x*j2
			x = 6*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))