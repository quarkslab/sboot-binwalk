import os
import struct
import binwalk.core.compat
import binwalk.core.common
import binwalk.core.plugin


class MCLFSignaturePlugin(binwalk.core.plugin.Plugin):

    '''
    MobiCore Load Format extractor plugin.
    '''
    MODULES = ['Signature']
    SIGNATURE_DESCRIPTION = "MobiCore Load Format"

    MCLF_HEADER_SIZE_V2 = 76
    MCLF_HEADER_SIZE_V23 = 96
    MCLF_TEXT_INFO_OFFSET = 128
    MCLF_TEXT_INFO_SIZE = 36

    MCLF_BINARY_MIN_SIZE = (MCLF_TEXT_INFO_OFFSET + MCLF_TEXT_INFO_SIZE)

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^mobicore load format',
                                           extension="mclf")

    def scan(self, result):
        '''
        Validate signature results.
        '''
        if result.valid:
            if result.description.startswith(self.SIGNATURE_DESCRIPTION):
                fd = self.module.config.open_file(result.file.name,
                                                  offset=result.offset)
                data = fd.read()
                fd.close()

                if len(data) < self.MCLF_BINARY_MIN_SIZE:
                    result.valid = False
                    return

                text_seg_len = struct.unpack("<I", data[0x34:0x38])[0]
                data_seg_len = struct.unpack("<I", data[0x3c:0x40])[0]

                # file contains 523 unknown bytes, determined empirically with
                # MobiCore trustlets
                size = text_seg_len + data_seg_len + 523
                if len(data) < size:
                    result.valid = False
                    return

                result.size = size
