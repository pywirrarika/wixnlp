#!/usr/bin/env python3
#
# Copyright (C) 2017.
# Author: Jesús Manuel Mager Hois
# e-mail: <fongog@gmail.com>
# Project website: http://turing.iimas.unam.mx/wix/

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from optparse import OptionParser
import morfessor


def train_seg(infile, outfile):
    io = morfessor.MorfessorIO()

    print("Open corpus file")
    train_data = list(io.read_corpus_file(infile))

    model_types = morfessor.BaselineModel()

    model_types.load_data(train_data, count_modifier=lambda x: 1)
    def log_func(x):
        return int(round(math.log(x + 1, 2)))

    print("Training data...")
    model_types.train_batch()

    print("Write bin file")
    io.write_binary_model_file(outfile, model_types)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input", help="read training file", metavar="FILE")
    parser.add_option("-o", "--output", dest="output", help="binary file for the model", metavar="FILE")
    (options, args) = parser.parse_args()
    print(options.input)
    print(options.output)
    train_seg(options.input, options.output)





