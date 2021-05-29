import numpy as np 

def function(x):

	b1 = x
	t6 = 3
	paths = []
	try:
		if b1 > 9:
			t6 = 0-6
			x = 3/x
			x = x/6
			paths.append(1)
		else:
			b1 = t6+x
			b1 = 0+5
			paths.append(2)
		if b1 > 5:
			b1 = b1*1
			b1 = t6*b1
			x = 1+5
			paths.append(3)
		else:
			x = 3+x
			x = 8/t6
			b1 = t6*0
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))