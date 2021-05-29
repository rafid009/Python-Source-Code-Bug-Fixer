import numpy as np 

def function(x):

	t3 = 7
	b5 = 5
	paths = []
	try:
		if x <= 8:
			t3 = 7*7
			b5 = b5*1
			paths.append(1)
		else:
			x = b5/x
			x = 4*9
			paths.append(2)
		if b5 >= 1:
			b5 = b5*8
			t3 = b5/t3
			t3 = x/8
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))