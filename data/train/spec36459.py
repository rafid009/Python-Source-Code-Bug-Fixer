import numpy as np 

def function(x):

	b9 = 9
	t5 = x
	paths = []
	try:
		if t5 < 1:
			x = x+6
			b9 = b9*2
			x = b9+x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if t5 >= 5:
			x = x-b9
			t5 = t5+x
			t5 = t5-x
			paths.append(3)
		else:
			t5 = t5+b9
			t5 = b9+t5
			t5 = t5*7
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		b9 = t5**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))