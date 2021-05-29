import numpy as np 

def function(x):

	t0 = 9
	e0 = x
	paths = []
	try:
		if x <= 2:
			t0 = e0/t0
			paths.append(1)
		else:
			t0 = 5/t0
			paths.append(2)
		if x > 0:
			x = x*0
			e0 = t0+t0
			paths.append(3)
		else:
			e0 = 4+0
			x = x+x
			x = x/t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))