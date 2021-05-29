import numpy as np 

def function(x):

	q0 = x
	t2 = x
	x = x
	paths = []
	try:
		if x <= 2:
			x = 2-0
			t2 = t2+8
			q0 = q0+x
			paths.append(1)
		else:
			x = 8*x
			t2 = 0+x
			paths.append(2)
		if q0 < 7:
			x = 2*8
			paths.append(3)
		else:
			t2 = 7/t2
			x = x+q0
			t2 = t2+t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))