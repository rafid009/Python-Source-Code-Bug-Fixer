import numpy as np 

def function(x):

	t4 = x
	d6 = 3
	paths = []
	try:
		if t4 <= 7:
			t4 = 4/d6
			x = 1*x
			d6 = x/d6
			paths.append(1)
		else:
			d6 = d6/2
			paths.append(2)
		if d6 > 1:
			d6 = d6*3
			paths.append(3)
		else:
			t4 = t4*2
			d6 = 9+d6
			t4 = t4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))