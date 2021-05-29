import numpy as np 

def function(x):

	t5 = x
	a9 = x
	paths = []
	try:
		if x > 0:
			t5 = t5+1
			a9 = 1/a9
			paths.append(1)
		else:
			a9 = a9+5
			a9 = x+9
			t5 = 5+t5
			paths.append(2)
		if t5 <= 2:
			a9 = a9*9
			t5 = t5*2
			t5 = t5+x
			paths.append(3)
		else:
			x = a9+x
			t5 = t5-5
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))