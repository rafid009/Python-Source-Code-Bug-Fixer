import numpy as np 

def function(x):

	b3 = x
	t5 = x
	paths = []
	try:
		if t5 <= 3:
			b3 = 4+b3
			paths.append(1)
		else:
			x = x*0
			t5 = t5*b3
			paths.append(2)
		if t5 > 5:
			x = b3-2
			b3 = 1+t5
			paths.append(3)
		else:
			t5 = 5-t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))