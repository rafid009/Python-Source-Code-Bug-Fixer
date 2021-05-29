import numpy as np 

def function(x):

	t5 = x
	f2 = x
	paths = []
	try:
		if t5 <= 9:
			x = x+x
			t5 = x*4
			x = f2/4
			paths.append(1)
		else:
			f2 = 4-8
			paths.append(2)
		if f2 >= 8:
			x = x*x
			paths.append(3)
		else:
			f2 = 4*f2
			f2 = f2*x
			t5 = t5-3
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		t5 = f2**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))