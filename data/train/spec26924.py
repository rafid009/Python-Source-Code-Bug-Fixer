import numpy as np 

def function(x):

	t2 = x
	f5 = 6
	paths = []
	try:
		if t2 >= 4:
			f5 = f5/6
			x = x+4
			t2 = 3-f5
			paths.append(1)
		else:
			t2 = t2-4
			x = x+5
			t2 = t2*8
			paths.append(2)
		if f5 >= 8:
			f5 = f5+5
			x = t2*x
			paths.append(3)
		else:
			t2 = x*7
			f5 = 0-f5
			x = x*t2
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