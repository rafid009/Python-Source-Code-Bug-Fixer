import numpy as np 

def function(x):

	r6 = x
	t0 = 9
	paths = []
	try:
		if r6 <= 3:
			r6 = 1+r6
			paths.append(1)
		else:
			t0 = t0-0
			paths.append(2)
		if x < 6:
			t0 = t0+x
			r6 = r6+8
			x = x+t0
			paths.append(3)
		else:
			x = 3+x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		t0 = r6**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))