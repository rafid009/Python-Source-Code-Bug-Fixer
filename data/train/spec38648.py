import numpy as np 

def function(x):

	a2 = x
	t3 = 7
	paths = []
	try:
		if a2 <= 8:
			t3 = t3/t3
			paths.append(1)
		else:
			a2 = 4/9
			x = 1/x
			a2 = a2*5
			paths.append(2)
		if t3 < 0:
			a2 = 1*4
			x = 6*9
			x = x+x
			paths.append(3)
		else:
			t3 = 1*t3
			t3 = t3*2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))