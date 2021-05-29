import numpy as np 

def function(x):

	t5 = 8
	p5 = 9
	paths = []
	try:
		if x < 7:
			p5 = 4+p5
			p5 = 4+t5
			paths.append(1)
		else:
			t5 = t5-t5
			paths.append(2)
		if p5 <= 6:
			p5 = 5/x
			paths.append(3)
		else:
			p5 = x*5
			t5 = 6-t5
			p5 = x+p5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))