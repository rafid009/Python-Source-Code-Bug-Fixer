import numpy as np 

def function(x):

	r4 = x
	t1 = 0
	paths = []
	try:
		if t1 <= 0:
			x = x+x
			t1 = x+2
			paths.append(1)
		else:
			r4 = 9+2
			paths.append(2)
		if r4 >= 6:
			r4 = 2-r4
			t1 = 2*t1
			r4 = r4+6
			paths.append(3)
		else:
			r4 = t1/2
			x = t1*0
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		t1 = r4**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))