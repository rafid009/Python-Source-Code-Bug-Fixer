import numpy as np 

def function(x):

	t3 = 6
	a1 = x
	paths = []
	try:
		if t3 < 0:
			a1 = 2+a1
			a1 = a1/1
			paths.append(1)
		else:
			a1 = a1/8
			a1 = a1/9
			t3 = 3/t3
			paths.append(2)
		if x > 2:
			t3 = 2-t3
			a1 = 3*t3
			paths.append(3)
		else:
			t3 = t3+t3
			a1 = a1-4
			t3 = t3+a1
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		a1 = t3**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))